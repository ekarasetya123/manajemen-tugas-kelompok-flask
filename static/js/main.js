// Simple script for responsive sidebar toggle on mobile
document.addEventListener('DOMContentLoaded', function() {
    // Toggle sidebar on small screens (optional)
    const sidebarToggle = document.createElement('button');
    sidebarToggle.innerHTML = '☰';
    sidebarToggle.style.position = 'fixed';
    sidebarToggle.style.top = '10px';
    sidebarToggle.style.left = '10px';
    sidebarToggle.style.zIndex = '1000';
    sidebarToggle.style.background = 'var(--kayu-jati-tua)';
    sidebarToggle.style.border = 'none';
    sidebarToggle.style.color = 'white';
    sidebarToggle.style.padding = '8px 12px';
    sidebarToggle.style.borderRadius = '4px';
    sidebarToggle.style.cursor = 'pointer';
    sidebarToggle.style.display = 'none';
    document.body.appendChild(sidebarToggle);

    const sidebar = document.querySelector('.sidebar');
    const mainContent = document.querySelector('.main-content');

    function updateToggleVisibility() {
        if (window.innerWidth <= 768) {
            // Mobile: hide sidebar by default
            sidebarToggle.style.display = 'block';
            sidebar.style.left = '-240px';
            mainContent.style.marginLeft = '0';
        } else {
            // Desktop: show sidebar
            sidebarToggle.style.display = 'none';
            sidebar.style.left = '0';
            mainContent.style.marginLeft = '240px';
        }
    }

    sidebarToggle.addEventListener('click', function() {
        if (sidebar.style.left === '0px') {
            // Hide sidebar
            sidebar.style.left = '-240px';
            mainContent.style.marginLeft = '0';
        } else {
            // Show sidebar
            sidebar.style.left = '0';
            mainContent.style.marginLeft = '240px';
        }
    });

    window.addEventListener('resize', updateToggleVisibility);
    updateToggleVisibility();

    // Initialize progress bars (if any)
    document.querySelectorAll('.progress-bar').forEach(function(bar) {
        const width = bar.getAttribute('data-width') || '0';
        bar.style.width = width + '%';
    });

    // Form validation enhancements (add required attribute to NIM field for numbers)
    document.querySelectorAll('input[pattern]').forEach(function(input) {
        input.addEventListener('input', function() {
            if (!input.value.match(input.pattern)) {
                input.setCustomValidity('Format tidak valid.');
            } else {
                input.setCustomValidity('');
            }
        });
    });
});